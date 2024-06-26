<template>
  <div>

    <div class="row" v-if="totalDebates > 0">

      <div class="col">
        <div class="card mt-3">
          <div class="card-body">
            <h5 class="mb-0 text-center" v-text="gettext('Ballots Status')"></h5>
          </div>
          <ul class="list-group list-group-flush">
            <li class="list-group-item text-secondary px-2" v-if="permissions.graph">
              <ballots-graph :graph-data="ballotStatuses"
                             :total-debates="totalDebates">
              </ballots-graph>
            </li>
            <li v-else class="list-group-item text-secondary text-center" v-text="gettext('No Results Yet')"></li>
          </ul>
        </div>
      </div>

    </div>

    <div class="row">

      <div class="col mt-3">
        <div class="card">
          <div class="card-body">
            <h5 class="mb-0" v-text="gettext('Latest Actions')"></h5>
          </div>
          <ul class="list-group list-group-flush" v-if="permissions.actionlog">
            <updates-list v-for="action in actionLogs"
                          :key="action.id"
                          :item="action"></updates-list>
          </ul>
          <ul class="list-group list-group-flush" v-else>
            <li class="list-group-item text-secondary" v-text="gettext('No Actions Yet')"></li>
          </ul>
        </div>
      </div>

      <div class="col mt-3">
        <div class="card">
          <div class="card-body">
            <h5 class="mb-0" v-text="gettext('Latest Results')"></h5>
          </div>
          <ul class="list-group list-group-flush" v-if="permissions.results">
            <updates-list v-for="ballot in ballotResults"
                          :key="ballot.id"
                          :item="ballot"></updates-list>
          </ul>
          <ul class="list-group list-group-flush" v-else>
            <li class="list-group-item text-secondary" v-text="gettext('No Confirmed Results Yet')"></li>
          </ul>
        </div>
      </div>

    </div>

  </div>
</template>

<script>
import _ from 'lodash'
import UpdatesList from '../../templates/graphs/UpdatesList.vue'
import WebSocketMixin from '../../templates/ajax/WebSocketMixin.vue'

export default {
  mixins: [WebSocketMixin],
  components: {
    UpdatesList,
    BallotsGraph: () => import('../../templates/graphs/BallotsGraph.vue'),
  },
  props: ['tournamentSlug', 'totalDebates', 'initialActions', 'initialBallots', 'initialGraphData', 'permissions'],
  data: function () {
    return {
      actionLogs: this.initialActions,
      ballotResults: this.initialBallots,
      ballotStatuses: this.initialGraphData,
    }
  },
  computed: {
    tournamentSlugForWSPath: function () {
      return this.tournamentSlug
    },
    sockets: function () {
      const sockets = []
      if (this.permissions.actionlog) {
        sockets.push('action_logs')
      }
      if (this.permissions.graph) {
        sockets.push('ballot_statuses')
      }
      if (this.permissions.results) {
        sockets.push('ballot_results')
      }
      return sockets
    },
  },
  methods: {
    handleSocketReceive: function (socketLabel, payload) {
      const data = payload.data
      if (socketLabel === 'ballot_statuses') {
        this.ballotStatuses.push(data) // Push blindly; graph will filter
        return
      }
      // Either action_logs or ballot_results
      const dataLabel = (socketLabel === 'ballot_results') ? 'ballotResults' : 'actionLogs'
      if (socketLabel === 'ballot_results') {
        if (data.confirmed === false || data.result_status !== 'C') {
          return // Don't show new results unless they are confirmed/confirmed
        }
      }
      // Check for duplicate log/results; do an inline replace if so
      const duplicateIndex = _.findIndex(this[dataLabel], i => i.id === data.id)
      if (duplicateIndex !== -1) {
        this[dataLabel][duplicateIndex] = data
      } else {
        // Add new item to front
        this[dataLabel].unshift(data)
        // Remove last item if at the limit
        if (this[dataLabel].length >= 15) {
          this[dataLabel].pop()
        }
      }
    },
  },
}
</script>
