## Example config files:

#### dev/encryption.json
```json
{
    "Rules": [
        {
            "ApplyServerSideEncryptionByDefault": {
                "SSEAlgorithm": "AES256"
            }
        }
    ]
}
```

---

#### dev/notification.json
```json
{
    "QueueConfigurations": [
        {
            "Filter": {
                "Key": {
                    "FilterRules": [
                        {
                            "Name": "prefix",
                            "Value": "folder01/"
                        }
                    ]
                }
            },
            "QueueArn": "arn:aws:sqs:us-east-1:123456701234:an-sqs-queue",
            "Events": [
                "s3:ObjectCreated:*",
                "s3:ObjectRestore:Completed"
            ]
        }
    ],
    "LambdaFunctionConfigurations": [
        {
            "LambdaFunctionArn": "arn:aws:lambda:us-east-1:123456701234:function:a-lambda-function",
            "Events": [
                "s3:ObjectCreated:*"
            ],
            "Filter": {
                "Key": {
                    "FilterRules": [
                        {
                            "Name": "prefix",
                            "Value": "folder02/"
                        }
                    ]
                }
            }
        },
        {
            "LambdaFunctionArn": "arn:aws:lambda:us-east-1:123456701234:function:another-lambda-function",
            "Events": [
                "s3:ObjectCreated:*"
            ],
            "Filter": {
                "Key": {
                    "FilterRules": [
                        {
                            "Name": "prefix",
                            "Value": "folder03/"
                        }
                    ]
                }
            }
        }
    ]
}
```

---

#### dev/policy.json
```json
{
    "Version": "2008-10-17",
    "Statement": [
        {
            "Sid": "S3BKT83994058743",
            "Effect": "Allow",
            "Principal": {
                "AWS": [
                    "arn:aws:iam::123456780123:role/SomeRole",
                    "arn:aws:iam::123456780123:role/AnotherRole"
                ]
            },
            "Action": [
                "s3:RestoreObject",
                "s3:AbortMultipartUpload",
                "s3:List*",
                "s3:Get*",
                "s3:Delete*",
                "s3:Put*"
            ],
            "Resource": [
                "arn:aws:s3:::some-bucket-name/*",
                "arn:aws:s3:::some-bucket-name"
            ]
        }
    ]
}
```

---

#### dev/properties.sh
```bash
bucket=some-bucket-name
profile=some-credential0-profile
```

---

#### dev/tags.json
```json
{
    "TagSet": [
        { "Key": "Name", "Value": "some-bucket-name" },
        { "Key": "ResourceOwner", "Value": "some.body@domain.com" },
        { "Key": "DeployedBy", "Value": "another.guy@domain.com" },
	    { "Key": "Project", "Value":"s3bkt" }
    ]
}
```
