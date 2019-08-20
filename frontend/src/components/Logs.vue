<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h2>Essential Links</h2>
  </div>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  #app {
    font-family: "Avenir", Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }

  #app .title {
    margin-bottom: 30px;
  }

  #app .items-per-page {
    height: 100%;
    display: flex;
    align-items: center;
    color: #337ab7;
  }

  #app .items-per-page label {
    margin: 0 15px;
  }

  /* Datatable CSS */
  .v-datatable-light .header-item {
    cursor: pointer;
    color: #337ab7;
    transition: color 0.15s ease-in-out;
  }

  .v-datatable-light .header-item:hover {
    color: #ed9b19;
  }

  .v-datatable-light .header-item.no-sortable{
    cursor: default;
  }
  .v-datatable-light .header-item.no-sortable:hover {
    color: #337ab7;
  }

  .v-datatable-light .header-item .th-wrapper {
    display: flex;
    width: 100%;
    height: 100%;
    font-weight: bold;
  }

  .v-datatable-light .header-item .th-wrapper.checkboxes {
    justify-content: center;
  }

  .v-datatable-light .header-item .th-wrapper .arrows-wrapper {
    display: flex;
    flex-direction: column;
    margin-left: 10px;
    justify-content: space-between;
  }

  .v-datatable-light .header-item .th-wrapper .arrows-wrapper.centralized {
    justify-content: center;
  }

  .v-datatable-light .arrow {
    transition: color 0.15s ease-in-out;
    width: 0;
    height: 0;
    border-left: 8px solid transparent;
    border-right: 8px solid transparent;
  }

  .v-datatable-light .arrow.up {
    border-bottom: 8px solid #337ab7;
  }

  .v-datatable-light .arrow.up:hover {
    border-bottom: 8px solid #ed9b19;
  }

  .v-datatable-light .arrow.down {
    border-top: 8px solid #337ab7;
  }

  .v-datatable-light .arrow.down:hover {
    border-top: 8px solid #ed9b19;
  }

  .v-datatable-light .footer {
    display: flex;
    justify-content: space-between;
    width: 500px;
  }
  /* End Datatable CSS */

  /* Pagination CSS */
  .v-datatable-light-pagination {
      list-style: none;
      display: flex;
      align-items: center;
      justify-content: flex-start;
      margin: 0;
      padding: 0;
      width: 300px;
      height: 30px;
    }

    .v-datatable-light-pagination .pagination-item {
      width: 30px;
      margin-right: 5px;
      font-size: 16px;
      transition: color 0.15s ease-in-out;
    }

    .v-datatable-light-pagination .pagination-item.selected {
      color: #ed9b19;
    }

    .v-datatable-light-pagination .pagination-item .page-btn {
      background-color: transparent;
      outline: none;
      border: none;
      color: #337ab7;
      transition: color 0.15s ease-in-out;
    }

    .v-datatable-light-pagination .pagination-item .page-btn:hover {
      color: #ed9b19;
    }

    .v-datatable-light-pagination .pagination-item .page-btn:disabled{
      cursor: not-allowed;
      box-shadow: none;
      opacity: .65;
    }
    /* END PAGINATION CSS */

    /* ITEMS PER PAGE DROPDOWN CSS */
    .item-per-page-dropdown {
      background-color: transparent;
      min-height: 30px;
      border: 1px solid #337ab7;
      border-radius: 5px;
      color: #337ab7;
    }
    .item-per-page-dropdown:hover {
      cursor: pointer;
    }
    /* END ITEMS PER PAGE DROPDOWN CSS */
</style>

<script>
export default {
  name: 'Logs',
  data () {
    return {
      msg: 'View Logs'
    }
  }
}
</script>
