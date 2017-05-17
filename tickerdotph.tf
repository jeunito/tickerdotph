variable "accountid" {}
variable "region" {}

provider "aws" {
	region = "${var.region}"
}

data "aws_iam_policy_document" "tph_lambda" {
	statement {
		actions = [ "sts:AssumeRole" ]
		principals {
			type = "Service"
			identifiers = [ "lambda.amazonaws.com" ]
		}
		effect = "Allow"
		sid = ""
	}
}

resource "aws_iam_role" "tph_www" {
	name = "tph_www"
	assume_role_policy = "${data.aws_iam_policy_document.tph_lambda.json}"
}

resource "aws_lambda_function" "tickerdotph" {
	filename = "tickerdotph.zip"
	function_name = "tickerdotph"
	handler =  "tickerdotph.main"
	runtime = "python2.7"
	description = "Backend for tickerdotph"
	role = "${aws_iam_role.tph_www.arn}"
	source_code_hash = "${base64sha256(file("tickerdotph.zip"))}"
}

resource "aws_api_gateway_rest_api" "tickerdotph" {
	name = "TickerDotPh"
}

resource "aws_api_gateway_resource" "tph_api_gateway_resource_fund" {
	rest_api_id = "${aws_api_gateway_rest_api.tickerdotph.id}"
	parent_id = "${aws_api_gateway_rest_api.tickerdotph.root_resource_id}"
	path_part = "fund"
}

resource "aws_api_gateway_method" "tph_api_gateway_method_get" {
	rest_api_id = "${aws_api_gateway_rest_api.tickerdotph.id}"
	resource_id = "${aws_api_gateway_resource.tph_api_gateway_resource_fund.id}"
	http_method = "GET"
	authorization = "NONE"
}

resource "aws_api_gateway_integration" "tph_api_gateway_integration_backend" {
	rest_api_id = "${aws_api_gateway_rest_api.tickerdotph.id}"
	resource_id = "${aws_api_gateway_resource.tph_api_gateway_resource_fund.id}"
	http_method = "${aws_api_gateway_method.tph_api_gateway_method_get.http_method}"
	integration_http_method = "POST"
	type = "AWS"
	uri = "arn:aws:apigateway:${var.region}:lambda:path/2015-03-31/functions/${aws_lambda_function.tickerdotph.arn}/invocations"
}

resource "aws_api_gateway_method_response" "tph_api_gateway_method_response_200" {
	rest_api_id = "${aws_api_gateway_rest_api.tickerdotph.id}"
	resource_id = "${aws_api_gateway_resource.tph_api_gateway_resource_fund.id}"
	http_method = "${aws_api_gateway_method.tph_api_gateway_method_get.http_method}"
	status_code = "200"
	response_models = {}
}

resource "aws_api_gateway_integration_response" "tph_api_gateway_integration_response_lambda" {
	rest_api_id = "${aws_api_gateway_rest_api.tickerdotph.id}"
	resource_id = "${aws_api_gateway_resource.tph_api_gateway_resource_fund.id}"
	http_method = "${aws_api_gateway_method.tph_api_gateway_method_get.http_method}"
	status_code = "${aws_api_gateway_method_response.tph_api_gateway_method_response_200.status_code}"
}

resource "aws_lambda_permission" "tph_aws_lambda_permission" {
  statement_id  = "AllowExecutionFromAPIGateway"
  action        = "lambda:InvokeFunction"
  function_name = "${aws_lambda_function.tickerdotph.arn}"
  principal     = "apigateway.amazonaws.com"

  source_arn = "arn:aws:execute-api:${var.region}:${var.accountid}:${aws_api_gateway_rest_api.tickerdotph.id}/*/${aws_api_gateway_method.tph_api_gateway_method_get.http_method}/fund"
}
