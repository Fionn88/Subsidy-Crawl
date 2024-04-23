#!/usr/bin/env bash
# exit on error
set -o errexit

STORAGE_DIR=/opt/render/project/.render


if [[ ! -d $STORAGE_DIR/chrome ]]; then
  #get latest version
  version=`curl http://chromedriver.storage.googleapis.com/LATEST_RELEASE`;
  echo 'Currently LATEST_RELEASE:' $version;
  #download the latest version chrome driver available as per the above line
  wget -N http://chromedriver.storage.googleapis.com/${version}/chromedriver_linux64.zip
  mkdir -p $STORAGE_DIR/chrome/
  unzip chromedriver_linux64.zip -d $STORAGE_DIR/chrome/
  chmod a+x $STORAGE_DIR/chrome/chromedriver
  #upgrade to latest google chrome 
  wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
  dpkg -x google-chrome-stable_current_amd64.deb $STORAGE_DIR/chrome
  rm ./google-chrome-stable_current_amd64.deb
  google_version=`google-chrome --version`;
  echo 'Google Chrome Version:' $google_version;
  echo 'Currently LATEST_RELEASE:' $version;
  echo 'End of the script'
else
  echo "...Using Chrome from cache"
fi


# add your own build commands...
poetry install --no-root