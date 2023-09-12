FROM public.ecr.aws/lambda/python:3.10

# # Install Tesseract and any other necessary dependencies
# RUN yum install -y tesseract-ocr

# # Copy your application code and requirements file
# COPY app.py requirements.txt ./

# # Install Python dependencies
# RUN python3.10 -m pip install -r requirements.txt -t .

# # Specify the Lambda function handler
# CMD ["app.lambda_handler"]


FROM public.ecr.aws/lambda/python:3.10

ENV LANG=ja_JP.UTF-8
WORKDIR ${LAMBDA_TASK_ROOT}
COPY app.py ./
COPY requirements.txt ./
# Install libgl1-mesa-glx package
RUN yum install -y mesa-libGL
RUN yum install -y mesa-libGL-devel
RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm \
    && yum update -y && yum install -y poppler-utils tesseract tesseract-langpack-jpn \
    && pip install -U pip && pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

CMD ["app.lambda_handler"]