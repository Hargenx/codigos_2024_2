import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/pessoas")
public class PessoaController {

    private final PessoaDAO pessoaDAO;

    public PessoaController(PessoaDAO pessoaDAO) {
        this.pessoaDAO = pessoaDAO;
    }

    @GetMapping
    public List<Pessoa> listarTodas() {
        return pessoaDAO.obterTodasPessoas();
    }

    @GetMapping("/{id}")
    public Pessoa obterPorId(@PathVariable int id) {
        return pessoaDAO.obterPessoaPorId(id);
    }

    @PostMapping
    public String criarPessoa(@RequestBody Pessoa pessoa) {
        pessoaDAO.inserirPessoa(pessoa);
        return "Pessoa criada com sucesso!";
    }

    @PutMapping("/{id}")
    public String atualizarPessoa(@PathVariable int id, @RequestBody Pessoa pessoa) {
        pessoaDAO.alterarPessoa(id, pessoa.getNome(), pessoa.getIdade(), pessoa.getAltura());
        return "Pessoa atualizada com sucesso!";
    }

    @DeleteMapping("/{id}")
    public String apagarPessoa(@PathVariable int id) {
        pessoaDAO.apagarPessoa(id);
        return "Pessoa removida com sucesso!";
    }
}