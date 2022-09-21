FROM python:3.10-slim


ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random

# copy project and set work directory
COPY . /code/
WORKDIR /code

# Install requirements
RUN pip install -r requirements.txt

CMD ["python", "-m", "bot"]
