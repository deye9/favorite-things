<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <div class="container">
      <table class="table table-bordered table-hover">
        <thead>
          <tr>
            <th nowrap> # </th>
            <th nowrap> Model </th>
            <th nowrap> Event </th>
            <th nowrap> Record ID </th>
            <th nowrap> Old Values </th>
            <th nowrap> New Values </th>
            <th nowrap> URL </th>
            <th nowrap> IP Address </th>
            <th nowrap> Date Created </th>
          </tr>
        </thead>
        <tbody>
          <tr :id="'row' + row.id" v-for="(row, index) in this.logs" v-bind:key="row.id">
            <td>{{++index}}</td>
            <td>{{row.model}}</td>
            <td>{{row.event}}</td>
            <td>{{row.record_id}}</td>
            <td>{{row.old_values}}</td>
            <td>{{row.new_values}}</td>
            <td>{{row.url}}</td>
            <td>{{row.ip_address}}</td>
            <td>{{row.created_date}}</td>
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
  name: 'Logs',
  data: () => ({
    logs: [],
    msg: 'Log'
  }),
  mounted () {
    this.getLogs()
  },
  methods: {
    getLogs () {
      apiService.getData('logs' + window.location.search).then((data) => {
        this.logs = data.logs
        console.log(this.logs)
        this.msg = `Viewing '${this.logs[0].model}' Log Records`
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
