{
    const inputs = []
    for (const pair of state.values) {
        inputs.push(pair[0] > pair[1] ? ">" : "<")
    }
    console.log(inputs)
    submit(inputs)
}
