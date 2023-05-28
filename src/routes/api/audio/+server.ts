import { json } from '@sveltejs/kit';
import type { RequestHandler } from './$types';
import {downloadAudio} from "$lib/server/services";

export const GET: RequestHandler = ({ url }) => {
    const id = url.searchParams.get('id');
     const err = downloadAudio(id)
    console.log('err: ', err)
    if (err) {
        return new Response(null, {status: 404})
    }
    return new Response(null, {status: 200})
};
