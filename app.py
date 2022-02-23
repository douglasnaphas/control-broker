#!/usr/bin/env python3
import os

import aws_cdk as cdk

from blueprint_pipelines.control_broker_eval_engine_stack import ControlBrokerEvalEngineStack

app = cdk.App()

env = cdk.Environment(
    account=os.getenv('CDK_DEFAULT_ACCOUNT'),
    region=os.getenv('CDK_DEFAULT_REGION')
)

# Input parameters
application_team_cdk_app = {
    'CodeCommitRepository' : 'opa-eval-serverless-cdk-source',
    'Branch' : 'master'
}



ControlBrokerEvalEngineStack(
    app,
    "ControlBrokerEvalEngineCdkStack",
    application_team_cdk_app = application_team_cdk_app,
    env = env
    )

app.synth()