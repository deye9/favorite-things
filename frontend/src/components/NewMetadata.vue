<template>
  <div class="row justify-content-center">
    <div class="col-md-8">
      <div class="card">
        <div class="card-header">{{ msg }}</div>
        <div class="card-body">
          <div class="form-group row">
            <label for="metadata_key" class="col-md-4 col-form-label text-md-right">Metadata Key</label>
            <div class="col-md-6">
              <input
                type="text"
                id="metadata_key"
                class="form-control"
                name="metadata_key"
                v-model="key"
                required
                autofocus
              />
            </div>
          </div>

          <div class="form-group row">
            <label for="metadata_value" class="col-md-4 col-form-label text-md-right">Metadata Value</label>
            <div class="col-md-6">
              <input
                type="text"
                id="metadata_value"
                class="form-control"
                name="metadata_value"
                v-model="value"
                required
                autofocus
              />
            </div>
          </div>

          <div class="col-md-6 offset-md-4">
            <button type="button" class="btn btn-primary" @click="newMetadata">Save</button>
          </div>

          <div id="message">
            {{message}}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { APIService } from '../APIService'
const apiService = new APIService()

export default {
  name: 'NewMetadata',
  data: () => ({
    key: '',
    value: '',
    message: '',
    metadata: [],
    msg: 'Create New Metadata'
  }),
  mounted () {
    this.getMetadata()
  },
  methods: {
    getMetadata () {
      apiService.getData('metadata').then(data => {
        this.metadata = data.metadata
      })
    },
    newMetadata () {
      // Check to make sure Metadata Key does not exist
      let IsValid = this.metadata.filter((metadata) => {
        return metadata.key === this.key
      })

      if (IsValid.length >= 1) {
        this.message = `Key '${this.key}' already exists.`
        return
      }

      apiService.createData('metadata', { key: this.key, value: this.value }).then(data => {
        if (data.status === 201 && data.data.status === 'success') {
          this.message = `Succesfully created key/value '${this.key}/${this.value}'`
          this.key = ''
          this.value = ''
        } else {
          this.message = data.data.errors
        }
      })
    }
  }
}
</script>
