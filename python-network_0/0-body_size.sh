cat > 0-body_size.sh <<'EOF'
#!/bin/bash
curl -s "$1" | wc -c
EOF
