import py
import os.path
from pypath import Path

def test_strpath(tmpdir):
    tmpdir.chdir()
    assert Path('foo').strpath == str(tmpdir.join('foo'))
    assert Path('/foo').strpath == '/foo'
    assert str(Path('/foo')) == '/foo'

def test_eq():
    p = Path('/tmp')
    assert p == Path('/tmp')
    assert p == '/tmp'
    assert p != '/tmp2'

def test_basename():
    p = Path('/tmp/foo.py')
    assert p.basename == 'foo.py'

def test_dirpath():
    p = Path('/tmp/foo.py')
    tmp = p.dirpath()
    assert isinstance(tmp, Path)
    assert tmp.strpath == '/tmp'

def test_join():
    p = Path('/tmp')
    assert p.join('foo') == '/tmp/foo'
    assert p.join('/foo') == '/foo'

def test_listdir(tmpdir):
    tmpdir.join('a.txt').write('')
    tmpdir.join('b.txt').write('')
    tmpdir.join('c.doc').write('')
    p = Path(tmpdir.strpath)
    files = p.listdir()
    assert files == [p.join('a.txt'), p.join('b.txt'), p.join('c.doc')]
    files = p.listdir('*.txt')
    assert files == [p.join('a.txt'), p.join('b.txt')]
    
def test_write_read(tmpdir):
    p = Path(tmpdir.strpath)
    foo = p.join('foo.txt')
    foo.write('hello')
    assert tmpdir.join('foo.txt').read() == 'hello'
    assert foo.read() == 'hello'
    
def test_ensure(tmpdir):
    p = Path(tmpdir.strpath)
    foo = p.join('foo').ensure(dir=True)
    assert os.path.isdir(foo.strpath)
    

def test_copy(tmpdir):
    p = Path(tmpdir.strpath)
    src = p.join('src')
    dst = p.join('dst')
    src.write('hello')
    src.copy(dst)
    assert dst.read() == 'hello'

    
