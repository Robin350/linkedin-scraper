from src.config import \
    rds, \
    tweepy, \
    aws, \
    s3


def test_aws_config():
    assert aws.ACCESS_KEY_ID is not None
    assert aws.SECRET_ACCESS_KEY is not None
    assert aws.DEFAULT_REGION is not None


def test_rds_config():
    assert rds.SQL is not None
    assert rds.HOST is not None
    assert rds.PORT is not None
    assert rds.USERNAME is not None
    assert rds.PASSWORD is not None
    assert rds.DATABASE is not None


def test_tweepy_config():
    if tweepy.BEARER_TOKEN is None:
        assert tweepy.CONSUMER_KEY is not None
        assert tweepy.CONSUMER_SECRET is not None
        assert tweepy.ACCESS_TOKEN is not None
        assert tweepy.ACCESS_SECRET is not None


def test_s3_config():
    assert s3.BUCKET_NAME is not None
