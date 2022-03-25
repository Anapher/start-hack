<script setup lang="ts">
import { ref } from 'vue'

defineProps<{ msg: string }>()

const count = ref(0)
</script>

<template>
  <div>
    <input type="text" placeholder="Name"/>
    <div> 
      <button>Submit</button>
    </div>
  </div>
</template>

<style scoped>
input[type='text']{
  padding:'5px'
}
button {
  margin-top: 20px;
}
</style>