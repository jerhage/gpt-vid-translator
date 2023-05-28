import { fail } from '@sveltejs/kit';

export const actions = {
    default: async ({ request }) => {
        const data = await request.formData();
        const id = data.get('id');

        if (!id) {
            fail(404, { id, missing: true });
        }

        const audio = await fetch()


        //
        // return {
        //     id
        // };
    }
};
