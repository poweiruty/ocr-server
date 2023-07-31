const board_number = window.location.pathname.split('/board/')[1]

$.ajax({
    "url": `/api/v1/boards/board/${board_number}`,
    "method": "GET",
    "timeout": 0,
}).done(function (board, result) {
    console.log(board);
    $('#author').text(board.author === null ? 'anonymous' : board.author.username);
    $('#title').val(board.title);
    $('#contents').val(board.contents);
    $('#test_ocr').val(board.ocr_result);    
    $('#loaded_file').attr('src', board.loaded_file);
    $('#created_at').val(board.created_at);
    $('#modified_at').val(board.modified_at);
});