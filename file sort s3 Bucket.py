
import boto3


class FileSorter(object):

    def __init__(self, BucketName='soumilnitinshah832019'):
        self.BucketName=BucketName
        self.client = boto3.client('s3')
        self.response = self.client.list_objects(Bucket=self.BucketName)

    @property
    def sort(self):

        data = []

        # Response to Get all Objects
        for x in self.response.get("Contents", None):
            data.append(x.get("Key", None))


        #Iterate Over Each File
        for x in data:
            print(x)

            if ('.jpg' in x) or ('.png' in x) or ('.jpeg' in x):

                # For Each File Get the Bytes Data
                response_new = self.client.get_object(Bucket=self.BucketName, Key=x)

                # Read the Bytes Data
                MyData = response_new["Body"].read()

                # Move That File into Folder called Image
                response = self.client.put_object(ACL='private',
                                                  Bucket='soumilnitinshah832019',
                                                  Body=MyData,
                                                  Key='Images/{}'.format(x))

                # Delete that File Outside Directory
                response = self.client.delete_object(Bucket=self.BucketName,Key=x)


            if ('.csv' in x):

                # For Each File Get the Bytes Data
                response_new = self.client.get_object(Bucket=self.BucketName, Key=x)

                # Read the Bytes Data
                MyData = response_new["Body"].read()

                # Move That File into Folder called Image
                response = self.client.put_object(ACL='private',
                                                  Bucket='soumilnitinshah832019',
                                                  Body=MyData,
                                                  Key='CSV/{}'.format(x))

                # Delete that File Outside Directory
                response = self.client.delete_object(Bucket=self.BucketName,Key=x)


            if ('.xlsx' in x):

                # For Each File Get the Bytes Data
                response_new = self.client.get_object(Bucket=self.BucketName, Key=x)

                # Read the Bytes Data
                MyData = response_new["Body"].read()

                # Move That File into Folder called Image
                response = self.client.put_object(ACL='private',
                                                  Bucket='soumilnitinshah832019',
                                                  Body=MyData,
                                                  Key='Excel/{}'.format(x))

                # Delete that File Outside Directory
                response = self.client.delete_object(Bucket=self.BucketName,Key=x)


            if ('.pdf' in x):

                # For Each File Get the Bytes Data
                response_new = self.client.get_object(Bucket=self.BucketName, Key=x)

                # Read the Bytes Data
                MyData = response_new["Body"].read()

                # Move That File into Folder called Image
                response = self.client.put_object(ACL='private',
                                                  Bucket='soumilnitinshah832019',
                                                  Body=MyData,
                                                  Key='PDF/{}'.format(x))

                # Delete that File Outside Directory
                response = self.client.delete_object(Bucket=self.BucketName,Key=x)

            if ('.mp4' in x):

                # For Each File Get the Bytes Data
                response_new = self.client.get_object(Bucket=self.BucketName, Key=x)

                # Read the Bytes Data
                MyData = response_new["Body"].read()

                # Move That File into Folder called Image
                response = self.client.put_object(ACL='private',
                                                  Bucket='soumilnitinshah832019',
                                                  Body=MyData,
                                                  Key='Video/{}'.format(x))

                # Delete that File Outside Directory
                response = self.client.delete_object(Bucket=self.BucketName,Key=x)

        print("Done ")


if __name__ == "__main__":
    obj = FileSorter()
    obj.sort