#!/bin/bash
VIDEO_ID=$1

[ -z "$VIDEO_ID" ] && echo "[Error]: Missing video id" && exit 1

yt-dlp "https://www.youtube.com/watch?v=$VIDEO_ID" -f "(ba)[ext=webm]/b[ext=webm]" -o "../tmp/%(id)s.%(ext)s" 2>&1

