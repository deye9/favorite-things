<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <div class="container">
      <table class="table table-bordered table-hover">
        <thead>
          <tr class="captionRow">
            <th colspan="5">
              <a href="/category/add">
                <button type="button" class="btn btn-primary">New Category</button>
              </a>
            </th>
          </tr>
          <tr>
            <th> # </th>
            <th nowrap> Name </th>
            <th nowrap> Created On </th>
            <th nowrap> Updated On </th>
            <th nowrap> Action </th>
          </tr>
        </thead>
        <tbody>
          <tr :id="'row' + row.id" v-for="(row, index) in this.categories" v-bind:key="row.id">
            <td>{{++index}}</td>
            <td>{{row.name}}</td>
            <td>{{row.created_date}}</td>
            <td>{{row.modified_date}}</td>
            <td nowrap>
              <a :href="'/category/edit/' + row.id">
                <button type="button" class="btn btn-primary">Edit</button>
              </a>
              <button type="button" class="btn btn-danger" @click="deleteCategory(row.id)">Delete</button>
              <a :href="'/logs?event=Category&record_id=' + row.id">
                <button type="button" class="btn btn-info">View Log</button>
              </a>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import {APIService} from '../APIService'
const apiService = new APIService()

export default {
  name: 'Categories',
  data: () => ({
    categories: [],
    msg: 'Categories Page'
  }),
  mounted () {
    this.getCategories()
  },
  methods: {
    getCategories () {
      apiService.getData('categories').then((data) => {
        this.categories = data.categories
      })
    },
    deleteCategory (pk, ctrl) {
      apiService.deleteData('categories', pk).then((data) => {
        if (data.status === 204) {
          var row = document.getElementById(`row${pk}`)
          row.parentNode.removeChild(row)
        }
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
table caption {
    line-height: 0;
    text-align: left;
}

table caption span {
    position: relative;
    left: 4px;
    top: 14px;
}

.captionRow th {
    text-align: right;
}
</style>
