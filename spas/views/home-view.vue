<script setup lang="ts">
import { ref } from 'vue';

const page = ref<string>('homepage')
</script>

<template>
  <main>
    <h1>This is the {{ page }}</h1>
    <ul>
      <li>✅ Typescript</li>
      <li class="red">✅ Sass</li>
    </ul>
  </main>
</template>

<style lang="scss" scoped>
$color: red;

.red {
  color: $color;
}
</style>
