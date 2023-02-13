# kivymobileapp


# create a google collab file and run the following  commands to get android apk

!pip install buildozer

!pip install cython==0.29.19


!sudo apt-get install -y \
    python3-pip \
    build-essential \
    git \
    python3 \
    python3-dev \
    ffmpeg \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libportmidi-dev \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    zlib1g-dev
    
    
    !sudo apt-get install libffi-dev
    
    !sudo apt-get -y install autoconf automake libtool cmake autoconf-archive build-essential
    
    !buildozer init
    
    # after init edit the buildozer.spec file properly
    
    !buildozer -v android debug
