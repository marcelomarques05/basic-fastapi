# FastAPI Basic Application

This code was generated from the 19 hours (yes, **hours**) Crash Course ```Python API Development - Comprehensive Course for Beginners``` on this [link](https://www.youtube.com/watch?v=0sOvCWFmrtA).

---

## General Information

> I will not describe anything related with the course here. This repo it's only to keep my study in some place, and maybe you can see as reference, but note that this is not following even best practices, it's a simple learning for REST API.

---

## Prerequisites

1. A GCP Project and a user with "Owner" role (I'm too lazy to see the specific roles for this course)
2. A Postgres database. I've created a free one to test on [ElephantSQL](https://www.elephantsql.com) DBaaS.
3. Docker installed on your host.
4. [Postman](https://www.postman.com) to test - _I've added my collection file to help_

I think that's all.

---

## Steps

### Local Execution

1. Copy the .env.example file to .env and put your information.

```bash
cp .env.example .env
```

2. Install `Python` libraries and start `uvicorn`:

```bash
# Install Libs
pip install -r requirements.txt

# Start Uvicorn
uvicorn app.main:app
````

> If everything works fine, you will be able to access through your web browser, the FastAPI swagger UI (<http://127.0.0.1:8000/docs>).
>
> You can start creating an user (```/create_user```) and then see all the endpoints and how it works.

### GCP Remote Execution

1. Enable the required APIs

```bash
gcloud services enable run.googleapis.com artifactregistry.googleapis.com
```

2. Create the Docker repository on Artifact Registry

```bash
gcloud artifacts repositories create ${REPO_NAME} \
  --project=${PROJECT_ID} \
  --repository-format=docker \
  --location=${DEFAULT_LOCATION} \
  --description=${REPO_DESCRIPTION}
```

3. Authorize the repository within Google SDK, build the image and push to GAR.

```bash
# Authorize
gcloud auth configure-docker ${DEFAULT_LOCATION}-docker.pkg.dev
# Build the image
docker build . --tag ${IMAGE_NAME}
# Tag the image to GAR
docker tag ${REPO_NAME} ${DEFAULT_LOCATION}-docker.pkg.dev/${PROJECT_ID}/${REPO_NAME}/${IMAGE_NAME}
# Push the image to GAR
docker push ${DEFAULT_LOCATION}-docker.pkg.dev/${PROJECT_ID}/${REPO_NAME}/${IMAGE_NAME}
```

4. Deploy the image to Cloud Run service on GCP

```bash
gcloud run deploy ${SERVICE_NAME} \
  --image ${DEFAULT_LOCATION}-docker.pkg.dev/${PROJECT_ID}/${REPO_NAME}/${IMAGE_NAME}:latest \
  --region=${DEFAULT_LOCATION}
  --allow-unauthenticated \
  --min-instances=1 \
  --max-instances=1 \
  --port 8000
```

5. Get your URL endpoint

```bash
gcloud run services describe ${SERVICE_NAME} \
  --region ${DEFAULT_LOCATION} \
  --format json \
  --flatten "status.address.url"

# Reference Output
[
  "https://service-name-ya2wotzz4q-uc.a.run.app"
]
```
