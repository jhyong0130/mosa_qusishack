FROM amazonlinux:2

# Install Python 3.8
RUN amazon-linux-extras enable python3.8 && \
    yum install -y python3.8 && \
    yum install -y python3-pip && \
    yum install -y zip && \
    yum clean all

# Install dependencies
RUN yum install -y gcc openssl-devel bzip2-devel libffi-devel make

# Set up PIP and Venv
RUN python3.8 -m pip install --upgrade pip && \
    python3.8 -m pip install virtualenv
RUN python3.8 -m venv base
RUN source base/bin/activate

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt -t ./python

# Zip it up for deployment.
RUN zip -r layer.zip ./python/
ENTRYPOINT ["/bin/bash", "-l"]
