import { spawn } from 'child_process';
import path from "path";

export const downloadAudio = (videoId: string) => {
    console.log('vid id: ', videoId)
    let err = null;
    const cmd = spawn(path.join(process.cwd(), 'src/lib/server/scripts/dl-yt-audio.sh' ), [videoId ?? '']);
    cmd.stderr.on('data', (data)=> {
        const str = data.toString('utf-8')
        err += str
    })
    cmd.on('close', ()=> {
        console.log('[FINISHED] - downloading audio')
    })

    return err
};