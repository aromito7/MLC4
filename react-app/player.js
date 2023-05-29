class Player{
    static types = ['HUMAN', 'AI', 'ML']
    constructor(typeNum, playerNumber){
        this.type = Player.types[typeNum]
        this.num = playerNumber
    }

    decide(board, active, player = this.player){
        const winImmediately = this.hasImmediateWin(board, active, 2)
        if(winImmediately >= 0) return winImmediately

        const blockOpponentWin = this.hasImmediateWin(board, active, 1)
        if(blockOpponentWin >= 0) return blockOpponentWin


        let validMoves = this.wontCauseImmediateWin(board, active, 1)
            .filter(move => active[move] >= 0)
        console.log(`valid moves: ${validMoves}`)

        let optimalMoves = this.maximalPotentialPaths(board, active, 2, validMoves)
        console.log(`optimal moves: ${optimalMoves}`)

        return optimalMoves[Math.floor(Math.random() * optimalMoves.length)]
    }

    static longestChainInDirection([x, y], [dx, dy], board, player){
        let chain = 0

        for(let i = 1; i <= 3; i++){
            const [tempX, tempY] = [x + i * dx, y + i * dy]
            if(tempX < 0 || tempX > 6 || tempY < 0 || tempY > 5 || board[tempY][tempX] !== player) break
            chain++
        }

        for(let i = -1; i >= -3; i--){
            const [tempX, tempY] = [x + i * dx, y + i * dy]
            if(tempX < 0 || tempX > 6 || tempY < 0 || tempY > 5 || board[tempY][tempX] !== player) break
            chain++
        }

        return chain
    }


    static longestChainAtLocation([x, y], board, player){
        if(y < 0) return -1
        let max = 0
        const directions = [[0, 1], [1, 1], [1, 0], [1, -1]]
        for(let [dx, dy] of directions){
            const chain = Player.longestChainInDirection([x, y], [dx, dy], board, player)
            max = chain > max ? chain : max
        }
        return max
    }

    static maximalPotentialPathAtLocationInDirection([x, y], [dx, dy], board, player){
        let maxChain = 0
        let chain = [player]
        // console.log([x, y], [dx, dy], player)
        for(let i = 1; i <= 3; i++){
            const [tempX, tempY] = [x + dx * i, y + dy * i]
            if(tempX < 0 || tempY < 0 || tempX > 6 || tempY > 5 || board[tempY][tempX] === 3 - player) break

            chain.push(board[tempY][tempX])
        }

        for(let i = -1; i >= -3; i--){
            const [tempX, tempY] = [x + dx * i, y + dy * i]

            if(tempX < 0 || tempY < 0 || tempX > 6 || tempY > 5 || board[tempY][tempX] === 3 - player) break

            chain.unshift(board[tempY][tempX])
        }

        // console.log(chain)

        for(let i = 0; i <= chain.length - 4; i++){
            const temp = chain.slice(i, i+4).filter(n => n === player).length

            if(temp > maxChain) maxChain = temp
        }

        return maxChain
    }

    static maximalPotentialPathAtLocation([x, y], board, player){
        const arrDelta = [[1, 0], [1, 1], [0, 1], [-1, 1]]

        const maxChains = arrDelta.map(([dx, dy]) => this.maximalPotentialPathAtLocationInDirection([x, y], [dx, dy], board, player))

        return maxChains.reduce( (acc, val) => val > acc? val: acc)
    }

    maximalPotentialPaths(board, active, player, validMoves = [0, 1, 2, 3, 4, 5, 6]){
        let maxChains = []
        let maxLength = 0
        let y
        const directions = [[0, 1], [1, 1], [1, 0], [1, -1]]
        for(let x of validMoves){
            y = active[x]
            if(y < 0) continue
            const temp = Player.maximalPotentialPathAtLocation([x, y], board, player)
            if(temp > maxLength){
                maxLength = temp
                maxChains = [x]
            }else if(temp === maxLength){
                maxChains.push(x)
            }
        }
        return maxChains
    }

    hasImmediateWin(board, active, player){
        let y
        const directions = [[0, 1], [1, 1], [1, 0], [1, -1]]
        for(let x = 0; x < active.length; x++){
            y = active[x]
            if(y < 0) continue
            if(Player.longestChainAtLocation([x, y], board, player) >= 3) return x
            /*
            for(let [dx, dy] of directions){
                const chain = Player.largestChainInDirection([x, y], [dx, dy], board, player)

                if(chain >= 3) {
                    return x
                }
            }
            */
        }
        return -1
    }

    wontCauseImmediateWin(board, active, player){
        let y
        let output = [0, 1, 2, 3, 4, 5, 6]
        const directions = [[0, 1], [1, 1], [1, 0], [1, -1]]
        for(let x = 0; x < active.length; x++){
            y = active[x] - 1
            if(y >= 0){
                for(let [dx, dy] of directions){
                    let chain = 0
                    for(let i = 1; i <= 3; i++){
                        const [tempX, tempY] = [x + i * dx, y + i * dy]
                        if(tempX < 0 || tempX > 6 || tempY < 0 || tempY > 5 || board[tempY][tempX] !== player) break
                        chain++
                    }

                    for(let i = -1; i >= -3; i--){
                        const [tempX, tempY] = [x + i * dx, y + i * dy]
                        if(tempX < 0 || tempX > 6 || tempY < 0 || tempY > 5 || board[tempY][tempX] !== player) break
                        chain++
                    }

                    if(chain >= 3) {
                        //console.log([x, y], [dx, dy], chain)
                        output[x] = -1
                    }
                }
            }
        }

        return output.filter((num, i) => num !== -1 && active[i] >= 0)
    }

}

module.exports = Player
