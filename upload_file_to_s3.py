import os
import boto3
from dotenv import load_dotenv

def getEnvironmentVariable(variable_name):
    return os.environ.get(variable_name)

# Carga de las variables de entorno desde el archivo .env
load_dotenv()

# Lectura de las variables de entorno
profile_name = getEnvironmentVariable("PROFILE")
region_name = getEnvironmentVariable("REGION")
bucket_name = getEnvironmentVariable("S3_BUCKET_NAME")

# Creación de la sesión de AWS
aws_session = boto3.Session(profile_name = profile_name, region_name = region_name)

# Creación de un cliente de S3
s3_client = aws_session.client("s3")

# Subida del fichero file_name al bucket bucket_name
file_name = "file_s3.txt"
object_name = os.path.basename(file_name)

response = s3_client.upload_file(file_name, bucket_name, object_name)

# Mensaje de confirmación de subida del archivo al bucket
print(f"Archvio {file_name} almacenado correctamente en el bucket {bucket_name}")