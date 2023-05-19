import os
import requests

def lambda_handler(event, context):
  """Converts a Word document to PDF and returns the path to the PDF file.

  Args:
    event: The event object from Lambda.
    context: The context object from Lambda.

  Returns:
    The path to the PDF file.
  """

  # Get the file name from the event object.
  file_name = event["file"]

  # Check if the file type is a Word document.
  if not file_name.endswith(".docx"):
    raise ValueError("File type must be .docx.")

  # Check if the file size is less than 5 MB.
  file_size = os.path.getsize(file_name)
  if file_size > 5 * 1024 * 1024:
    raise ValueError("File size must be less than 5 MB.")

  # Convert the Word document to PDF.
  with open(file_name, "rb") as f:
    pdf_content = docx2pdf.convert(f)

  # Save the PDF file to the S3 bucket.
  s3_client = boto3.client("s3")
  s3_client.put_object(
    Bucket=os.environ["OUTPUT_BUCKET"],
    Key=file_name.replace(".docx", ".pdf"),
    Body=pdf_content,
  )

  # Return the path to the PDF file.
  return f"{os.environ['OUTPUT_BUCKET']}/{file_name.replace('.docx', '.pdf')}"
