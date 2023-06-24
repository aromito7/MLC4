const Grid = () => {
    console.log("Grid: ")
    return (
      <div id="grid" class="grid">
        {
          Array(7).fill().map((row, i) => <Row/>)
        }
      </div>
    )
  }

const Row = () => {
console.log("Row")
return (
    <div class="row">
    {
        Array(6).fill().map(square => <Square/>)
    }
    </div>
)
}


const Square = () => {
    console.log("Square displayed")
    return(
        <div class="square empty"/>
    )
}

export default Grid
