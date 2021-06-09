FROM python

RUN apt-get update \
    && apt-get install -y texlive-latex-recommended

COPY template.tex template.tex

COPY requirements.txt requirements.txt
COPY archive.py archive.py

COPY entrypoint.sh entrypoint.sh
RUN chmod +x entrypoint.sh

CMD ["./entrypoint.sh"]