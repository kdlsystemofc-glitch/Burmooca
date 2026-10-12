"""Gera as bordas-assinatura (SVG, decorativas) de cada cliente: edge-top.svg e edge-bottom.svg.
Mesmo contrato da torn-paper da base: viewBox 1440x40, preserveAspectRatio=none, a cor de cima/baixo é o
--bg-cream do cliente e o resto é transparente (mostra a faixa escura)."""
import math, os, random, sys

W, H = 1440, 40


def pts_wave(base, amp, period, phase=0.0, step=10, jitter=0.0, seed=1):
    rnd = random.Random(seed)
    out = []
    for x in range(0, W + step, step):
        y = base + amp * math.sin(2 * math.pi * x / period + phase) + (rnd.uniform(-jitter, jitter) if jitter else 0)
        out.append((x, max(0.0, min(H, y))))
    return out


def path_from(points, close_to):
    d = f'M 0 {close_to} ' + ' '.join(f'L {x:.1f} {y:.1f}' for x, y in points) + f' L {W} {close_to} Z'
    return d


def flip(points):
    return [(x, H - y) for x, y in points]


def svg(paths):
    body = ''.join(f'<path d="{d}" fill="{c}"/>' for d, c in paths)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" preserveAspectRatio="none">{body}</svg>'


def flames(base, seed):
    """Línguas de fogo: picos irregulares subindo (y menor = mais alto)."""
    rnd = random.Random(seed)
    out, x = [(0, base)], 0
    while x < W:
        w = rnd.uniform(26, 52)
        h = rnd.uniform(10, base - 2)
        out += [(x + w * 0.35, base - h * 0.55), (x + w * 0.5, base - h), (x + w * 0.62, base - h * 0.5), (x + w, base)]
        x += w
    return [(min(W, a), max(0, b)) for a, b in out]


def write(dirpath, top, bottom):
    open(os.path.join(dirpath, 'edge-top.svg'), 'w', encoding='utf-8').write(top)
    open(os.path.join(dirpath, 'edge-bottom.svg'), 'w', encoding='utf-8').write(bottom)


def burmooca(d):
    cream, lettuce = '#f7f0de', '#3f9a3c'
    lt = pts_wave(20, 5, 120, step=8)          # onda de alface (verde)
    cr = pts_wave(12, 4, 120, phase=1.2, step=8)  # creme por cima
    top = svg([(path_from(lt, 0), lettuce), (path_from(cr, 0), cream)])
    bottom = svg([(path_from(flip(lt), H), lettuce), (path_from(flip(cr), H), cream)])
    write(d, top, bottom)


def sogra(d):
    cream, flame, glow = '#fbf1e1', '#e8590c', '#ffb81c'
    # embaixo da faixa escura (borda inferior): chamas laranja/amarelas subindo para dentro da faixa
    f1 = flames(40, 7)
    f2 = [(x, min(H, y + 9)) for x, y in flames(40, 11)]
    bottom = svg([(path_from(f1, H), flame), (path_from(f2, H), glow),
                  (path_from(pts_wave(36, 1.5, 300, step=20), H), cream)])
    # topo: borda ondulada simples (fumaça), creme
    top = svg([(path_from(pts_wave(10, 6, 260, step=10, jitter=1.2, seed=3), 0), cream)])
    write(d, top, bottom)


if __name__ == '__main__':
    kind, d = sys.argv[1], sys.argv[2]
    {'burmooca': burmooca, 'sogra': sogra}[kind](d)
    print('edges ->', d)
