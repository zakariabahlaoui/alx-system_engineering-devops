# Distributed Web Infrastructure

![Image of a distributed web infrastructure](1-distributed_web_infrastructure.png)

[Visit Board](https://miro.com/app/board/uXjVOfI6jcU=/)

## Description

This is a distributed web infrastructure that atttempts to reduce the traffic to the primary server by distributing some of the load to a replica server with the aid of a server responsible for balancing the load between the two servers (primary and replica).

## Specifics About This Infrastructure

- The distribution algorithm the load balancer is configured with and how it works.<br/>The HAProxy load balancer is configured with the _Round Robin_ distribution algorithm. This algorithm works by using each server behind the load balancer in turns, according to their weights. It’s also probably the smoothest and most fair algorithm as the servers’ processing time stays equally distributed. As a dynamic algorithm, _Round Robin_ allows server weights to be adjusted on the go.
- The setup enabled by the load-balancer.<br/>The HAProxy load-balancer is enabling an _Active-Passive_ setup rather than an _Active-Active_ setup. In an _Active-Active_ setup, the load balancer distributes workloads across all nodes in order to prevent any single node from getting overloaded. Because there are more nodes available to serve, there will also be a marked improvement in throughput and response times. On the other hand, in an _Active-Passive_ setup, not all nodes are going to be active (capable of receiving workloads at all times). In the case of two nodes, for example, if the first node is already active, the second node must be passive or on standby. The second or the next passive node can become an active node if the preceding node is inactive.
- How a database _Primary-Replica_ (_Master-Slave_) cluster works.<br/>A _Primary-Replica_ setup configures one server to act as the _Primary_ server and the other server to act as a _Replica_ of the _Primary_ server. However, the _Primary_ server is capable of performing read/write requests whilst the _Replica_ server is only capable of performing read requests. Data is synchronized between the _Primary_ and _Replica_ servers whenever the _Primary_ server executes a write operation.
- The difference between the _Primary_ node and the _Replica_ node in regard to the application.<br/>The _Primary_ node is responsible for all the write operations the site needs whilst the _Replica_ node is capable of processing read operations, which decreases the read traffic to the _Primary_ node.

## Issues With This Infrastructure

- There are multiple SPOF (Single Point Of Failure).<br/>For example, if the Primary MySQL database server is down, the entire site would be unable to make changes to the site (including adding or removing users). The server containing the load balancer and the application server connecting to the primary database server are also SPOFs.
- Security issues.<br/>The data transmitted over the network isn't encrypted using an SSL certificate so hackers can spy on the network. There is no way of blocking unauthorized IPs since there's no firewall installed on any server.
- No monitoring.<br/>We have no way of knowing the status of each server since they're not being monitored.
