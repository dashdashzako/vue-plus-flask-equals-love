<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'

import MiniMessage from './components/footer-message.vue';
</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <nav>
        <ul>
          <li>
            <a href="/admin">Admin</a>
          </li>
          <li>
            <RouterLink to="/">Home</RouterLink>
          </li>
          <li>
            <RouterLink to="/about">About</RouterLink>
          </li>
        </ul>
      </nav>
    </div>
  </header>

  <RouterView />

  <MiniMessage />
</template>
