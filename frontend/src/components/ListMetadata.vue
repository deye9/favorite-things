<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <div class="container">
      <table class="table table-bordered table-hover">
        <thead>
          <tr class="captionRow">
            <th colspan="6">
              <a href="/metadata/add">
                <button type="button" class="btn btn-primary">New Metadata</button>
              </a>
            </th>
          </tr>
          <tr>
            <th> # </th>
            <th> Key </th>
            <th> Value </th>
            <th> Created On </th>
            <th> Updated On </th>
            <th> Action </th>
          </tr>
        </thead>
        <tbody>
          <tr :id="'row' + row.id" v-for="row in this.metadata" v-bind:key="row.id">
            <td>{{row.id}}</td>
            <td>{{row.key}}</td>
            <td>{{row.value}}</td>
            <td>{{row.created_date}}</td>
            <td>{{row.modified_date}}</td>
            <td>
              <a :href="'/metadata/edit/' + row.id">
                <button type="button" class="btn btn-primary">Edit</button>
              </a>
              <button type="button" class="btn btn-danger" @click="deleteMetadata(row.id)">Delete</button>
              <a :href="'/logs/' + row.id">
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
  name: 'Metadata',
  data: () => ({
    metadata: [],
    msg: 'Metadata'
  }),
  mounted () {
    this.getMetadata()
  },
  methods: {
    getMetadata () {
      apiService.getData('metadata').then((data) => {
        this.metadata = data.metadata
      })
    },
    deleteMetadata (pk, ctrl) {
      apiService.deleteData('metadata', pk).then((data) => {
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
