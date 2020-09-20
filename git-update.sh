REPO_DIR=/home/eremeykin/projects/personal/i3configs

function cp_file {
  ORIG_FILE=$1
  DEST_FILE=$(dirname "${REPO_DIR}${ORIG_FILE}")
  mkdir -p $DEST_FILE
  sudo cp $ORIG_FILE $DEST_FILE
}

function cp_dir {
  ORIG_DIR=$1
  DEST_DIR=$(dirname "${REPO_DIR}${ORIG_DIR}")
  mkdir -p $DEST_DIR
  sudo cp -r $ORIG_DIR $DEST_DIR
}

cp_file /usr/share/X11/xorg.conf.d/40-libinput.conf
cp_dir ~/.config/i3/
cp_file ~/.xsessionrc
cp_file /etc/X11/xorg.conf
cp_file /etc/i3status.conf
