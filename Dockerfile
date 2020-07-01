FROM ubuntu:latest
LABEL maintainer="michaellundquist7@gmail.com"

RUN apt-get -yq update

#timezone stuff
RUN apt-get -y install tzdata
RUN echo "America/New_York" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata

#ubuntu dependencies
RUN apt-get -yq install --fix-missing apt-transport-https git gnuplot graphviz python3-distutils python3-pip
RUN apt-get -yq install texlive-font-utils texlive-latex-extra texlive-latex-recommended

#downloading and installing rmtoo
RUN git clone https://github.com/florath/rmtoo.git /usr/share/doc/rmtoo

RUN python3 -m pip install -r /usr/share/doc/rmtoo/requirements.txt
RUN python3 -m pip install /usr/share/doc/rmtoo