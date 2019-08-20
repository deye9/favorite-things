<template>
  <div id="app">
    <br />
    <router-view>
      <router-link v-bind:to="'/'">Items</router-link>
      <router-link v-bind:to="'/logs'">Logs</router-link>
      <router-link v-bind:to="'/metadata'">Metadata</router-link>
      <router-link v-bind:to="'/category'">New Category</router-link>
      <router-link v-bind:to="'/categories'">Categories</router-link>
      <router-link v-bind:to="'/edit_category'">Edit Category</router-link>
    </router-view>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
