FROM ubuntu:latest
LABEL maintainer="michaellundquist7@gmail.com"

RUN apt-get -yq update
RUN apt-get -yq upgrade
RUN apt-get install -qy apt-transport-https
RUN apt-get -yq update
RUN apt-get -yq upgrade
RUN apt-get -y install tzdata
RUN echo "America/New_York" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata
RUN apt-get -yq install --fix-missing apt-utils git
RUN apt-get -yq install --fix-missing gnuplot graphviz python3-distutils python3-pip python-virtualenv
RUN apt-get -yq install texlive-font-utils texlive-latex-extra texlive-latex-recommended
RUN python3 -m pip install --upgrade pip setuptools wheel
RUN python3 -m pip install --only-binary=numpy,scipy scipy numpy
RUN python3 -m pip install six~=1.12
RUN git clone https://github.com/florath/rmtoo.git /usr/share/doc/rmtoo
RUN python3 -m pip install /usr/share/doc/rmtoo