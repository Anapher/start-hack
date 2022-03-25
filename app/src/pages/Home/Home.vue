<template>
<div class="justify-center	 w-1/3 grid grid-rows-2 gap-3">
    <p class="text-2xl text-black">Welcome To OpenBicycle</p>
    <button @click="$router.replace({ path: '/search' })" class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded">Let's Get Started.</button>
</div>
</template>
<!--| |-->
<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'Home',
    components: {

    },
    data() {
        return {

        };
    },
    setup() {

    },
    async created() {
    },
    methods: {

    }
})
</script>
<!--| |-->
<style scoped>

</style>