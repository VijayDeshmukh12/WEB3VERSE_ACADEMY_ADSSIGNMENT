import docx2pdf
import os
import requests

def convert_word_to_pdf(file_name, output_bucket):
  """Converts a Word document to PDF.

  Args:
    file_name: The name of the Word document.
    output_bucket: The name of the S3 bucket where the PDF file will be stored.

  Returns:
    The path to the PDF file.
  """

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
    Bucket=output_bucket,
    Key=file_name.replace(".docx", ".pdf"),
    Body=pdf_content,
  )

  # Return the path to the PDF file.
  return f"{output_bucket}/{file_name.replace('.docx', '.pdf')}"
