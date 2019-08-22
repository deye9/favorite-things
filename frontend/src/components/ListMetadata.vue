<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <div class="container">
      <table class="table table-bordered table-hover">
        <thead>
          <tr class="captionRow">
            <th colspan="6">
              <router-link class="btn btn-primary" to="/metadata/add">New Metadata</router-link>
            </th>
          </tr>
          <tr>
            <th> # </th>
            <th nowrap> Key </th>
            <th nowrap> Value </th>
            <th nowrap> Created On </th>
            <th nowrap> Updated On </th>
            <th nowrap> Action </th>
          </tr>
        </thead>
        <tbody>
          <tr :id="'row' + row.id" v-for="(row, index) in this.metadata" v-bind:key="row.id">
            <td>{{++index}}</td>
            <td>{{row.key}}</td>
            <td>{{row.value}}</td>
            <td>{{row.created_date}}</td>
            <td>{{row.modified_date}}</td>
            <td nowrap>
              <router-link class="btn btn-primary" v-bind:to="'/metadata/edit/' + row.id">Edit</router-link>
              <button type="button" class="btn btn-danger" @click="deleteMetadata(row.id)">Delete</button>
              <router-link class="btn btn-info" v-bind:to="'/logs?event=Metadata&record_id=' + row.id">View Log</router-link>
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
