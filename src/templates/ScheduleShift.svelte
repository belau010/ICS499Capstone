<script>
  import API from "../API";

  let searchString = "";
  let users = [];
  let selectedUser = null;
  let startTime = null;
  let endTime = null;
  let notes = "";

  async function onSearchClick() {
    users = await API.user.search(searchString);
  }
</script>

<main>
  Schedule Shift
  <hr />
  <div style="display: flex; flex-direction: row">
    <div style="width: 50%; padding: 8px">
      <input placeholder="Search by last name..." bind:value={searchString} />
      <button on:click={onSearchClick}> Search </button>
      <hr />
      {#each users as user}
        <button
          style={user == selectedUser
            ? "background-color:mediumseagreen;"
            : ""}
          on:click={() => {
            selectedUser = user;
          }}
        >
          {user.lastName}, {user.firstName}
        </button>
        <br />
      {/each}
    </div>
    <div style="width: 50%; padding: 8px">
      Start Time: <br />
      <input bind:value={startTime} type="datetime-local" id="shift-starttime-input" /><br />
      End Time: <br />
      <input bind:value={endTime} type="datetime-local" id="shift-endtime-input" /><br />
      Notes:<br />
      <textarea bind:value={notes} style="resize: none" rows="4"></textarea>
    </div>
  </div>
  <button on:click={()=>{
    API.shift.create(selectedUser.id, startTime, endTime, notes);
  }}> Schedule </button>
</main>

<style>
</style>
