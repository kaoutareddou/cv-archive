FROM python

RUN apt-get update \
    & apt-get install -y texlive-latex-recommended

COPY template.tex template.tex

COPY archive.py archive.py

ENTRYPOINT ["python3", "archive.py"]