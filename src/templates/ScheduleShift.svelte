<script>
  import API from "../API";

  let searchString = "";
  let users = [];

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
        <div>
          {user.lastName}, {user.firstName}
        </div>
        <br />
      {/each}
    </div>
    <div style="width: 50%; padding: 8px">
      Start Time: <br />
      <input type="datetime-local" id="shift-starttime-input" /><br />
      End Time: <br />
      <input type="datetime-local" id="shift-endtime-input" /><br />
      Notes:<br />
      <textarea style="resize: none" rows="4"></textarea>
    </div>
  </div>
  <button> Schedule </button>
</main>

<style>
</style>
