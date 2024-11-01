<?php

namespace App\Models;

//use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Pessoa extends Model
{
    protected $table = 'pessoas';
    protected $primaryKey = 'id';
    protected $fillable = ['nome', 'email', 'telefone', 'endereco', 'data_nascimento'];
}
