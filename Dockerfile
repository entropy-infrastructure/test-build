FROM public.ecr.aws/docker/library/python:3.11

#
WORKDIR /code

#
COPY ./requirements.txt /code/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install fastapi uvicorn

#
COPY ./app /code/app

EXPOSE 80

#
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
