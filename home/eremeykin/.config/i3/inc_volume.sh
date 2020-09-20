INC_STEP=5
MAX_VOL=100
CURR_VOL=$(pactl list sinks | grep '^[[:space:]]Volume:' | head -n $(( $SINK + 1 )) | tail -n 1 | sed -e 's,.* \([0-9][0-9]*\)%.*,\1,')
NEXT_VOL=$((CURR_VOL+INC_STEP))

if [ "$NEXT_VOL" -le "$MAX_VOL" ]; then
  pactl set-sink-volume 0 +${INC_STEP}%
else
  pactl set-sink-volume 0 ${MAX_VOL}%
fi
