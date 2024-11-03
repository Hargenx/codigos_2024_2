<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\pessoaController;


Route::get('/', [pessoaController::class, 'index'])->name('listar');
Route::get('id/{id}', [pessoaController::class, 'show'])->name('buscar');
Route::get('/form', [pessoaController::class, 'create'])->name('formulario');
Route::post('/salvar', [pessoaController::class, 'posts'])->name('salvarPessoa');
Route::get('/pessoa/{pessoa}/editar', [pessoaController::class, 'edit'])->name('editar');
Route::put('/pessoa/{pessoa}', [pessoaController::class, 'update'])->name('atualizar');
Route::delete('/pessoa/{pessoa}', [pessoaController::class, 'destroy'])->name('excluir');
Route::get('/pessoa/confirmar-exclusao/{pessoa}', [pessoaController::class, 'confirmarExclusao'])->name('confirmarExclusao');



/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "web" middleware group. Make something great!
|


Route::get('/', function () {
    return view('welcome');
});
*/