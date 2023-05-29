var assert = require('assert');
var Player = require('../player')
//const {checkForWin} = require('../index')
describe('decide', function () {
  const AI = new Player(1, 2)

  const active1 = [4, 4, 4, 5, 4, 4, 4]
  const board1 = [[0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [2, 2, 2, 0, 1, 1, 1]];

  const active2 = [4, 4, 4, 2, 2, 3, 4]
  const board2 = [[0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 2, 0, 0],
                  [0, 0, 0, 1, 1, 2, 0],
                  [2, 2, 2, 1, 1, 2, 1]];

  describe('largestChainAtLocation', function(){
    it('should detect three in a row for both players', function () {
      assert.equal(Player.longestChainAtLocation([3, 5], board1, 2), 3);
      assert.equal(Player.longestChainAtLocation([3, 5], board1, 1), 3);
    });
    it('should detect three in a row for both players', function () {
      assert.equal(Player.longestChainAtLocation([3, 2], board2, 2), 2);
      assert.equal(Player.longestChainAtLocation([3, 2], board2, 1), 3);
    });
  });


  describe('hasImmediateWin', function () {
    const AI = new Player(1, 2)

    const activeBottom = [5, 5, 5, 5, 5, 5, 5]
    const activeTop = [0, 0, 0, 0, 0, 0, 0]

    const active1 = [4, 4, 4, 5, 4, 4, 4]
    const board1 = [[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [2, 2, 2, 0, 1, 1, 1]];

    const active2 = [2, 5, 5, 5, 5, 5, 2]
    const board2 = [[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [2, 0, 0, 0, 0, 0, 1],
                    [2, 0, 0, 0, 0, 0, 1],
                    [2, 0, 0, 0, 0, 0, 1]]

    const board3 = [[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 2, 1, 0],
                    [0, 0, 0, 2, 1, 0, 0],
                    [0, 0, 2, 1, 0, 0, 0],
                    [0, 2, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]]


    const active4 = [4, 5, 4, 3, 3, 4, 3]
    const board4 = [[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 2, 2, 0, 2],
                    [1, 0, 1, 1, 2, 2, 1]];

    const active5 = [2, 2, 2, 2, 2, 2, 2]
    const board5 = [[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 2, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 2, 1, 0, 0, 0],
                    [0, 2, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]]

    const board6 = [[0, 0, 0, 0, 0, 0, 0],
                    [0, 1, 2, 0, 0, 0, 0],
                    [0, 0, 1, 2, 0, 0, 0],
                    [0, 0, 0, 1, 2, 0, 0],
                    [0, 0, 0, 0, 1, 2, 0],
                    [0, 0, 0, 0, 0, 0, 0]]

    const active7 = [2, 2, 2, 2, 2, 2, 2]
    const board7 = [[0, 0, 0, 0, 0, 0, 0],
                    [0, 1, 2, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 2, 0, 0],
                    [0, 0, 0, 0, 1, 2, 0],
                    [0, 0, 0, 0, 0, 0, 0]]

    it('should detect a horizontal win on the end', function () {
      assert.equal(AI.hasImmediateWin(board1, active1, 2), 3);
      assert.equal(AI.hasImmediateWin(board1, active1, 1), 3);
    });
    it('should detect a horizontal win in the middle', function () {
      assert.equal(AI.hasImmediateWin(board4, active4, 2), 5);
      assert.equal(AI.hasImmediateWin(board4, active4, 1), 1);
    });

    it('should detect a vertical win on the end', function () {
      assert.equal(AI.hasImmediateWin(board2, active2, 2), 0);
      assert.equal(AI.hasImmediateWin(board2, active2, 1), 6);
    });

    it('should detect a diagonal up win on the end', function () {
      assert.equal(AI.hasImmediateWin(board3, activeTop, 2), 5);
      assert.equal(AI.hasImmediateWin(board3, activeTop, 1), 6);
    });
    it('should detect a diagonal up win on either end', function () {
      assert.equal(AI.hasImmediateWin(board3, activeBottom, 2), 0);
      assert.equal(AI.hasImmediateWin(board3, activeBottom, 1), 1);
    });
    it('should detect a diagonal up win in the middle', function () {
      assert.equal(AI.hasImmediateWin(board5, active5, 2), 3);
      assert.equal(AI.hasImmediateWin(board5, active5, 1), 4);
    });

    it('should detect a diagonal down win on the end', function () {
      assert.equal(AI.hasImmediateWin(board6, activeTop, 2), 1);
      assert.equal(AI.hasImmediateWin(board6, activeTop, 1), 0);
    });
    it('should detect a diagonal down win on either end', function () {
      assert.equal(AI.hasImmediateWin(board6, activeBottom, 2), 6);
      assert.equal(AI.hasImmediateWin(board6, activeBottom, 1), 5);
    });
    it('should detect a diagonal down win in the middle', function () {
      assert.equal(AI.hasImmediateWin(board7, active7, 2), 3);
      assert.equal(AI.hasImmediateWin(board7, active7, 1), 2);
    });
  });

  describe('wontCauseImmediateWin', function () {
    const AI = new Player(1, 2)

    const active1 = [5, 1, -1, -1, 1, 2, 4]
    const board1 = [[0, 0, 2, 1, 0, 0, 0],
                    [0, 0, 1, 2, 0, 0, 0],
                    [0, 2, 2, 1, 1, 0, 0],
                    [0, 2, 2, 1, 1, 1, 0],
                    [0, 1, 1, 1, 2, 2, 0],
                    [0, 2, 1, 2, 1, 2, 2]];

    const active2 = [-1, 1, 4, 2, 5, 2, 1]
    const board2 = [[1, 0, 0, 0, 0, 0, 0],
                    [2, 0, 0, 0, 0, 0, 0],
                    [1, 2, 0, 0, 0, 0, 1],
                    [1, 1, 0, 1, 0, 1, 2],
                    [2, 2, 0, 2, 0, 2, 2],
                    [2, 2, 1, 1, 0, 1, 1]];



    it('should avoid moves that give opponent immediate win on the end', function () {
      assert.equal(AI.wontCauseImmediateWin(board1, active1, 1).toString(), [4].toString());
      assert.equal(AI.wontCauseImmediateWin(board1, active1, 2).toString(), [1, 5, 6].toString());
    });

    it('should avoid moves that give opponent immediate win in the middle', function () {
      assert.equal(AI.wontCauseImmediateWin(board2, active2, 1).toString(), [1, 3, 5, 6].toString());
      assert.equal(AI.wontCauseImmediateWin(board2, active2, 2).toString(), [1, 3, 5, 6].toString());
    });

  });

  describe('findsLongestPotentialPathAtLocationInDirection', function () {
    const AI = new Player(1, 2)

    const active1 = [5, 5, 5, 2, 5, 1, 5]
    const board1 = [[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 1, 0, 2, 0],
                    [0, 0, 0, 2, 0, 2, 0],
                    [0, 0, 0, 1, 0, 2, 0]];

    const active2 = [4, 4, 4, -1, 4, 4, -1]
    const board2 = [[0, 0, 0, 2, 0, 0, 1],
                    [0, 0, 0, 1, 0, 0, 1],
                    [0, 0, 0, 1, 0, 0, 2],
                    [0, 0, 0, 1, 0, 0, 2],
                    [0, 0, 0, 1, 0, 0, 1],
                    [1, 1, 2, 2, 2, 1, 1]];

    const board3 = [[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 1],
                    [1, 0, 0, 0, 0, 0, 2],
                    [2, 0, 0, 2, 0, 0, 1],
                    [2, 0, 0, 1, 2, 0, 1],
                    [2, 2, 1, 2, 1, 0, 1]];


    it('should recognize that it would have two horizontal chips towards a connect four even with a gap between them', function () {
      assert.equal(Player.maximalPotentialPathAtLocationInDirection([0, 5], [1, 0], board1, 1), 2);
      assert.equal(Player.maximalPotentialPathAtLocationInDirection([1, 5], [1, 0], board1, 1), 2);
      assert.equal(Player.maximalPotentialPathAtLocationInDirection([2, 5], [1, 0], board1, 1), 2);
      assert.equal(Player.maximalPotentialPathAtLocationInDirection([4, 5], [1, 0], board1, 1), 2);
    });
    it('should not recognize a horizontal two in a row that is blocked from expanding into a connect four', function () {
      assert.equal(Player.maximalPotentialPathAtLocationInDirection([4, 5], [1, 0], board1, 2), 0);
      assert.equal(Player.maximalPotentialPathAtLocationInDirection([6, 5], [1, 0], board1, 2), 0);
    });
    it('should recognize a vertical chain that can be expanded from one that cannot', function () {
      assert.equal(Player.maximalPotentialPathAtLocationInDirection([3, 2], [0, 1], board1, 1), 2);
      assert.equal(Player.maximalPotentialPathAtLocationInDirection([5, 1], [0, 1], board1, 1), 0);
    });
    it('should recognize a diagonal chain that can be expanded from one that cannot', function () {
      assert.equal(Player.maximalPotentialPathAtLocationInDirection([4, 4], [1, 1], board2, 1), 3);
      assert.equal(Player.maximalPotentialPathAtLocationInDirection([5, 4], [-1, 1], board2, 1), 0);
      assert.equal(Player.maximalPotentialPathAtLocationInDirection([5, 4], [1, 1], board2, 1), 3);

      assert.equal(Player.maximalPotentialPathAtLocationInDirection([4, 4], [1, 1], board2, 2), 0);
      assert.equal(Player.maximalPotentialPathAtLocationInDirection([4, 4], [-1, 1], board2, 2), 3);
      assert.equal(Player.maximalPotentialPathAtLocationInDirection([5, 4], [-1, 1], board2, 2), 0);
    });

    it('should recognize a diagonal chain that can be expanded from one that cannot', function () {
      assert.equal(Player.maximalPotentialPathAtLocationInDirection([3, 2], [0, 1], board1, 1), 2);
      assert.equal(Player.maximalPotentialPathAtLocationInDirection([5, 1], [0, 1], board1, 1), 0);
    });

    it('should recognize a diagonal three in a row', function () {
      assert.equal(Player.maximalPotentialPathAtLocationInDirection([4, 3], [-1, 1], board3, 1), 3);
      assert.equal(Player.maximalPotentialPathAtLocationInDirection([4, 3], [1, -1], board3, 1), 3);
    });
  });

  describe('findsLongestPotentialPathAtLocation', function () {
    const AI = new Player(1, 2)

    const active1 = [5, 5, 5, 4, 5, 5, 5]
    const board1 = [[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0, 2, 0]];

    const active2 = [4, 4, 4, 5, 5, 4, 4]
    const board2 = [[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [1, 2, 2, 0, 0, 1, 1]];

    const active3 = [1, 4, 4, 2, 3, 5, 0]
    const board3 = [[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 1],
                    [1, 0, 0, 0, 0, 0, 2],
                    [2, 0, 0, 2, 0, 0, 1],
                    [2, 0, 0, 1, 2, 0, 1],
                    [2, 2, 1, 2, 1, 0, 1]];


    it('should recognize that it would have two chips towards a connect four even with a gap between them', function () {
      assert.equal(Player.maximalPotentialPathAtLocation([0, 5], board1, 1), 2);
      assert.equal(Player.maximalPotentialPathAtLocation([1, 5], board1, 1), 2);
      assert.equal(Player.maximalPotentialPathAtLocation([2, 5], board1, 1), 2);
      assert.equal(Player.maximalPotentialPathAtLocation([4, 5], board1, 1), 2);
    });
    it('should not recognize a two in a row that is blocked from expanding into a connect four', function () {
      assert.equal(Player.maximalPotentialPathAtLocation([4, 5], board1, 2), 1);
      assert.equal(Player.maximalPotentialPathAtLocation([6, 5], board1, 2), 1);
    });
    it('should recognize a diagonal three in a row', function () {
      assert.equal(Player.maximalPotentialPathAtLocation([4, 3], board1, 1), 3);
      assert.equal(Player.maximalPotentialPathAtLocation([3, 2], board1, 1), 2);
    });
  });



  describe('findsLongestPotentialPath', function () {
    const AI = new Player(1, 2)

    const active1 = [5, 5, 5, 4, 5, 5, 5]
    const board1 = [[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0]];

    const active2 = [4, 4, 4, 5, 5, 4, 4]
    const board2 = [[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [1, 2, 2, 0, 0, 1, 1]];

    const active3 = [1, 4, 4, 2, 3, 5, 0]
    const board3 = [[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 1],
                    [1, 0, 0, 0, 0, 0, 2],
                    [2, 0, 0, 2, 0, 0, 1],
                    [2, 0, 0, 1, 2, 0, 1],
                    [2, 2, 1, 2, 1, 0, 1]];


    it('should recogonize that any two pieces within a four block span can count towards a potential connect four', function () {
      assert.equal(AI.maximalPotentialPaths(board1, active1, 1).toString(), [0, 1, 2, 3, 4, 5, 6].toString());
      assert.equal(AI.maximalPotentialPaths(board1, active1, 2).toString(), [0, 1, 2, 3, 4, 5, 6].toString());
    });
    it('should recognize a potential horizontal three in a row', function () {
      assert.equal(AI.maximalPotentialPaths(board2, active2, 1).toString(), [3, 4].toString());
      assert.equal(AI.maximalPotentialPaths(board2, active2, 2).toString(), [3, 4].toString());
    });
    it('should recognize a potential diagonal three in a row', function () {
      assert.equal(AI.maximalPotentialPaths(board2, active2, 1).toString(), [4].toString());
      assert.equal(AI.maximalPotentialPaths(board2, active2, 2).toString(), [2, 5].toString());
    });
  });
});
