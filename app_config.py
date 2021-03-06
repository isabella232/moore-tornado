#!/usr/bin/env python

"""
Project-wide application configuration.

DO NOT STORE SECRETS, PASSWORDS, ETC. IN THIS FILE.
They will be exposed to users. Use environment variables instead.
See get_secrets() below for a fast way to access them.
"""

import os

"""
NAMES
"""
# Project name used for display
PROJECT_NAME = 'Zoom In On Oklahoma Tornado Damage'

# Project name used for paths on the filesystem and in urls
# Use dashes, not underscores
PROJECT_SLUG = 'moore-oklahoma-tornado-damage'

# The name of the repository containing the source
REPOSITORY_NAME = 'moore-tornado'

"""
DEPLOYMENT
"""
PRODUCTION_S3_BUCKETS = ['apps.npr.org', 'apps2.npr.org']
PRODUCTION_SERVERS = ['cron.nprapps.org']

STAGING_S3_BUCKETS = ['stage-apps.npr.org']
STAGING_SERVERS = ['cron-staging.nprapps.org']

# Should code be deployed to the web/cron servers?
DEPLOY_TO_SERVERS = False

# Should the crontab file be installed on the servers?
# If True, DEPLOY_TO_SERVERS must also be True
DEPLOY_CRONTAB = False

# Should the service configurations be installed on the servers?
# If True, DEPLOY_TO_SERVERS must also be True
DEPLOY_SERVICES = False

# These variables will be set at runtime. See configure_targets() below
S3_BUCKETS = []
SERVERS = []
DEBUG = True

"""
COPY EDITING
"""
COPY_GOOGLE_DOC_KEY = '0AjlIKRG8DtTqdDZKdVZJT0pTTVRaaTJ0RzhZaUo2akE'

"""
SHARING
"""
PROJECT_DESCRIPTION = 'Survey the damage from the tornado that struck Moore, Oklahoma.'
SHARE_URL = 'https://%s/%s/' % (PRODUCTION_S3_BUCKETS[0], PROJECT_SLUG)


TWITTER = {
    'TEXT': PROJECT_DESCRIPTION,
    'URL': SHARE_URL,
    'IMAGE_URL': 'https://apps.npr.org/moore-oklahoma-tornado-damage/img/moore-ok-twitter.png'
}

FACEBOOK = {
    'TITLE': PROJECT_NAME,
    'URL': SHARE_URL,
    'DESCRIPTION': PROJECT_DESCRIPTION,
    'IMAGE_URL': 'https://apps.npr.org/moore-oklahoma-tornado-damage/img/moore-ok.png',
    'APP_ID': '138837436154588'
}

NPR_DFP = {
    'STORY_ID': '171421875',
    'TARGET': '\/news_politics;storyid=171421875'
}

"""
SERVICES
"""
GOOGLE_ANALYTICS_ID = 'UA-5828686-4'

"""
Utilities
"""
def get_secrets():
    """
    A method for accessing our secrets.
    """
    env_var_prefix = PROJECT_SLUG.replace('-', '')

    secrets = [
        '%s_TUMBLR_APP_KEY' % env_var_prefix,
        '%s_TUMBLR_OAUTH_TOKEN' % env_var_prefix,
        '%s_TUMBLR_OAUTH_TOKEN_SECRET' % env_var_prefix,
        '%s_TUMBLR_APP_SECRET' % env_var_prefix
    ]

    secrets_dict = {}

    for secret in secrets:
        # Saves the secret with the old name.
        secrets_dict[secret.replace('%s_' % env_var_prefix, '')] = os.environ.get(secret, None)

    return secrets_dict

def configure_targets(deployment_target):
    """
    Configure deployment targets. Abstracted so this can be
    overriden for rendering before deployment.
    """
    global S3_BUCKETS
    global SERVERS
    global DEBUG

    if deployment_target == 'production':
        S3_BUCKETS = PRODUCTION_S3_BUCKETS
        SERVERS = PRODUCTION_SERVERS
        DEBUG = False
    else:
        S3_BUCKETS = STAGING_S3_BUCKETS
        SERVERS = STAGING_SERVERS
        DEBUG = True

"""
Run automated configuration
"""
DEPLOYMENT_TARGET = os.environ.get('DEPLOYMENT_TARGET', None)

configure_targets(DEPLOYMENT_TARGET)
