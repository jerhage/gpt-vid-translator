<script lang="ts">
	import { enhance } from '$app/forms';
	export let form;

	$: console.log('the form: ', form);
</script>

<h1>YT Audio Translator</h1>
<form
	method="POST"
	use:enhance={({ data }) => {
		const videoUrl = data.get('videoUrl');
		console.log('the input: ', videoUrl);
		const id = new URL(videoUrl).searchParams.get('v');

		id && data.set('id', id);
		return async ({ update }) => {
			await update();
		};
	}}
>
	<input type="text" name="videoUrl" placeholder="https://www.youtube.com/watch?v=" />
	<button>Send</button>
</form>
{#if form?.id}
	<h1>Your id is: {form.id}</h1>
{/if}
